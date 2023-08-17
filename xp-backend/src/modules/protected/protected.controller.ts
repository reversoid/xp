import { Controller, Get, UseGuards } from '@nestjs/common';
import { ProtectedService } from './protected.service';
import { ProtectedGuard } from './guards/protected.guard';
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import { Experiment } from '../experiment/entities/experiment.entity';

@ApiTags('Protected')
@Controller('protected')
@UseGuards(ProtectedGuard)
export class ProtectedController {
  constructor(private protectedService: ProtectedService) {}

  @ApiOperation({ description: 'Get unfinished experiments for all users' })
  @ApiResponse({
    description: 'Unfinished experiments',
    type: Experiment,
    isArray: true,
  })
  @Get('unfinished_experiments')
  async getUnfinishedExperiments() {
    return this.protectedService.getAllUnfinishedExperiments();
  }
}
