import { Controller, Get, UseGuards } from '@nestjs/common';
import { ProtectedService } from './protected.service';
import { ProtectedGuard } from './guards/protected.guard';

@Controller('protected')
@UseGuards(ProtectedGuard)
export class ProtectedController {
  constructor(private protectedService: ProtectedService) {}

  @Get('unfinished_experiments')
  async getUnfinishedExperiments() {
    return this.protectedService.getAllUnfinishedExperiments();
  }
}
