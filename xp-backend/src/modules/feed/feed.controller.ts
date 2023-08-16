import {
  Controller,
  Get,
  Param,
  Put,
  Request,
  UseGuards,
} from '@nestjs/common';
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';
import { FeedService } from './feed.service';
import { NumericIdParamDTO } from 'src/shared/dto/id.param.dto';

@Controller('feed')
export class FeedController {
  constructor(private readonly feedService: FeedService) {}

  @Get('experiments')
  @UseGuards(AuthGuard)
  async getExperiments(@Request() { user }: { user: User }) {
    return this.feedService.getExperiments(user.id);
  }

  @Put('experiment/:id/views')
  @UseGuards(AuthGuard)
  async markExperimentAsSeen(
    @Request() { user }: { user: User },
    @Param() { id }: NumericIdParamDTO,
  ) {
    return this.feedService.markExperimentAsSeen(user.id, id);
  }
}
